"""API of fair-python-cookiecutter-demo."""

from fastapi import FastAPI, HTTPException

from fair_python_cookiecutter_demo.lib import CalcOperation, calculate

app = FastAPI()


@app.get("/calculate/{op}")
def calc(op: CalcOperation, x: int, y: int = 0):
    """Return result of calculation on two integers."""
    try:
        return calculate(op, x, y)

    except (ZeroDivisionError, ValueError, NotImplementedError) as e:
        if isinstance(e, ZeroDivisionError):
            err = f"Cannot divide x={x} by y=0!"
        else:
            err = str(e)
        raise HTTPException(status_code=422, detail=err) from e


def run():
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
