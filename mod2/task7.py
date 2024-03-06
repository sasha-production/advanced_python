from flask import Flask

app = Flask(__name__)

storage = {}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    year, month, day = int(date[:4]), int(date[4:6]), int(date[6:])
    if not (storage.get(year) and storage[year].get(month) and storage[year][month].get(day)):
        storage.setdefault(year, {}).setdefault(month, {}).setdefault(day, 0)
    storage[year][month][day] += number
    expenses = storage[year][month][day]
    return f"траты за {day}/{month}/{year} {expenses} p."


@app.route("/calculate/<int:year>")
def calculate_year(year: int):
    months = storage.get(year)
    if not months:
        return '0'
    expenses = sum([sum(days.values()) for month, days in months.items()])
    return f"траты за {year} год: {expenses}"

@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int):
    if not (storage.get(year) and storage[year].get(month)):
        return '0'
    expenses = sum(storage[year][month].values())
    return f"траты за {year}/{month}: {expenses} p."


if __name__ == "__main__":
    app.run(debug=True)