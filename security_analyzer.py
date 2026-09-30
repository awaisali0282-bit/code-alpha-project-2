from flask import Flask, request, jsonify
from flask_cors import CORS
import re

app = Flask(__name__)
CORS(app)


def analyze_code(code):

    findings = []

    # SQL Injection
    if re.search(
        r"(SELECT|INSERT|UPDATE|DELETE).*[\+\%].*(request|input|user)",
        code,
        re.IGNORECASE
    ):
        findings.append({
            "type": "SQL Injection",
            "severity": "HIGH",
            "line": "Potential user input directly combined with SQL.",
            "recommendation": "Use parameterized queries or prepared statements."
        })

    # Hardcoded password
    if re.search(
        r"(password|passwd|pwd)\s*=\s*[\"']",
        code,
        re.IGNORECASE
    ):
        findings.append({
            "type": "Hardcoded Credential",
            "severity": "HIGH",
            "line": "A password or credential appears to be hardcoded.",
            "recommendation": "Store secrets in environment variables or a secure secret manager."
        })

    # eval()
    if re.search(
        r"\beval\s*\(",
        code
    ):
        findings.append({
            "type": "Dangerous eval()",
            "severity": "HIGH",
            "line": "eval() can execute dynamically supplied code.",
            "recommendation": "Avoid eval() and use safer parsing methods."
        })

    # os.system
    if re.search(
        r"os\.system\s*\(",
        code
    ):
        findings.append({
            "type": "Command Execution",
            "severity": "MEDIUM",
            "line": "os.system() executes operating-system commands.",
            "recommendation": "Validate input carefully and prefer safer subprocess APIs."
        })

    # Debug mode
    if re.search(
        r"debug\s*=\s*True",
        code,
        re.IGNORECASE
    ):
        findings.append({
            "type": "Debug Mode Enabled",
            "severity": "MEDIUM",
            "line": "Debug mode is enabled.",
            "recommendation": "Disable debug mode in production environments."
        })

    # Weak MD5
    if re.search(
        r"\bmd5\b",
        code,
        re.IGNORECASE
    ):
        findings.append({
            "type": "Weak Hashing Algorithm",
            "severity": "MEDIUM",
            "line": "MD5 is present in the code.",
            "recommendation": "Use a modern password-hashing algorithm such as Argon2, bcrypt, or scrypt."
        })

    # HTTP URL
    if re.search(
        r"http://",
        code,
        re.IGNORECASE
    ):
        findings.append({
            "type": "Insecure HTTP",
            "severity": "LOW",
            "line": "An HTTP URL was detected.",
            "recommendation": "Use HTTPS when transmitting sensitive information."
        })

    return findings


@app.route("/api/analyze", methods=["POST"])
def analyze():

    data = request.get_json()

    if not data or "code" not in data:
        return jsonify({
            "error": "No code provided"
        }), 400

    code = data["code"]

    findings = analyze_code(code)

    high = sum(
        1 for item in findings
        if item["severity"] == "HIGH"
    )

    medium = sum(
        1 for item in findings
        if item["severity"] == "MEDIUM"
    )

    low = sum(
        1 for item in findings
        if item["severity"] == "LOW"
    )

    return jsonify({
        "total": len(findings),
        "high": high,
        "medium": medium,
        "low": low,
        "findings": findings
    })


@app.route("/api/status")
def status():

    return jsonify({
        "status": "online",
        "tool": "Secure Code Review"
    })


if __name__ == "__main__":

    print("=" * 55)
    print("       SECURE CODE REVIEW ANALYZER")
    print("=" * 55)
    print("Backend: http://127.0.0.1:5000")
    print("Status: ONLINE")
    print("=" * 55)

    app.run(
        host="127.0.0.1",
        port=5000,
        debug=False
    )