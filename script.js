const API_URL = "http://127.0.0.1:5000";


// ======================================
// ANALYZE CODE
// ======================================

async function analyzeCode() {

    const code =
        document.getElementById("codeInput").value;

    if (!code.trim()) {

        alert("Please enter some code first.");

        return;
    }


    try {

        const response = await fetch(
            API_URL + "/api/analyze",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify({
                    code: code
                })
            }
        );


        const data =
            await response.json();


        if (data.error) {

            alert(data.error);

            return;
        }


        document.getElementById(
            "highCount"
        ).textContent = data.high;


        document.getElementById(
            "mediumCount"
        ).textContent = data.medium;


        document.getElementById(
            "lowCount"
        ).textContent = data.low;


        displayResults(data.findings);

    }

    catch (error) {

        console.error(error);

        setStatus(
            "BACKEND OFFLINE",
            false
        );

    }

}


// ======================================
// DISPLAY RESULTS
// ======================================

function displayResults(findings) {

    const results =
        document.getElementById("results");


    if (!findings.length) {

        results.innerHTML = `

            <div class="secure-message">

                <strong>
                    ✓ NO COMMON ISSUES DETECTED
                </strong>

                <span>
                    The analyzer did not identify
                    any of its configured patterns.
                </span>

            </div>

        `;

        return;
    }


    results.innerHTML = "";


    findings.forEach(item => {

        const card =
            document.createElement("div");

        card.className =
            "finding " +
            item.severity.toLowerCase();


        card.innerHTML = `

            <div class="finding-top">

                <strong>
                    ${safe(item.type)}
                </strong>

                <span>
                    ${safe(item.severity)}
                </span>

            </div>

            <p>
                ${safe(item.line)}
            </p>

            <small>
                Recommendation:
                ${safe(item.recommendation)}
            </small>

        `;


        results.appendChild(card);

    });

}


// ======================================
// SAFE TEXT
// ======================================

function safe(value) {

    const element =
        document.createElement("div");

    element.textContent =
        value ?? "-";

    return element.innerHTML;

}


// ======================================
// BACKEND STATUS
// ======================================

async function checkStatus() {

    try {

        const response =
            await fetch(
                API_URL + "/api/status"
            );

        if (response.ok) {

            setStatus(
                "SYSTEM ONLINE",
                true
            );

        }

    }

    catch {

        setStatus(
            "BACKEND OFFLINE",
            false
        );

    }

}


// ======================================
// STATUS UI
// ======================================

function setStatus(
    message,
    online
) {

    document.getElementById(
        "statusText"
    ).textContent = message;


    const dot =
        document.getElementById(
            "statusDot"
        );


    dot.className =
        online ? "online" : "offline";

}


// ======================================
// INITIAL CHECK
// ======================================

checkStatus();

setInterval(
    checkStatus,
    3000
);