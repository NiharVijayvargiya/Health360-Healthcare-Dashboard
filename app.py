from flask import Flask, render_template

app = Flask(__name__)

# ---------------------------------------------------------------
# Tableau Public ke baad yahan apne links paste karo.
# Tableau Public page -> "Share" -> "Copy Link" (sirf URL, embed code nahi)
# Example:
# "https://public.tableau.com/views/Health360/Dashboard"
# ---------------------------------------------------------------
DASHBOARD_URL = "https://public.tableau.com/views/Health360_17934468105130/Health360Dashboard"
STORY_URL = "https://public.tableau.com/views/Health360_17934468105130/Health360Story"

KPIS = {
    "patients": "5,000",
    "diabetes": "1,746",
    "heart_disease": "1,499",
    "stroke": "1,243",
}


@app.route("/")
def home():
    return render_template(
        "index.html",
        dashboard_url=DASHBOARD_URL,
        story_url=STORY_URL,
        kpis=KPIS,
    )


if __name__ == "__main__":
    app.run(debug=True)
