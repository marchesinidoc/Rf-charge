from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template con interfaccia responsive e campo per duty cycle
HTML = """
<!doctype html>
<html lang="it">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Calcolatore Carica RF</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        margin: 20px;
        max-width: 500px;
        padding: 10px;
      }
      input, select, button {
        padding: 10px;
        margin: 10px 0;
        width: 100%;
        box-sizing: border-box;
        font-size: 1rem;
      }
      h2 {
        font-size: 1.4rem;
        text-align: center;
      }
      .result {
        margin-top: 20px;
        font-weight: bold;
        color: blue;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <h2>Calcolatore Carica Elettrica RF</h2>
    <form method="post">
      <label>Modalità:</label>
      <select name="mode">
        <option value="Q">Calcola Q (Carica)</option>
        <option value="t">Calcola t (Tempo)</option>
      </select>

      <label>Tensione (V):</label>
      <input type="number" step="any" name="voltage" required>

      <label>Impedenza (Z in Ohm):</label>
      <input type="number" step="any" name="impedance" required>

      <label>Tempo (s) o Carica (C):</label>
      <input type="number" step="any" name="time_or_charge" required>

      <label>Duty cycle (decimale, es. 0.04 standard PRF):</label>
      <input type="number" step="any" name="duty_cycle" value="0.04" required>

      <button type="submit">Calcola</button>
    </form>

    {% if result %}
      <div class="result">{{ result }}</div>
    {% endif %}
  </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        try:
            mode = request.form["mode"]
            V = float(request.form["voltage"])
            Z = float(request.form["impedance"])
            val = float(request.form["time_or_charge"])
            duty = float(request.form["duty_cycle"])

            if mode == "Q":
                # Val è tempo: calcola Q = (V * t * DC) / Z
                Q = (V * val * duty) / Z
                result = f"Carica (Q): {Q:.4f} C"
            elif mode == "t":
                # Val è Q: calcola t = (Q * Z) / (V * DC)
                t = (val * Z) / (V * duty)
                result = f"Tempo (t): {t:.2f} s"
        except Exception as e:
            result = "Errore nei dati inseriti."

    return render_template_string(HTML, result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
