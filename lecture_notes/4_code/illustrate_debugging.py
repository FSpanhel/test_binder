# make a simple function to debug
def sum_(a: float, b: float) -> float:
    "Returns the sum of a and b."
    a, b = parse_args(a, b)
    return a + b


def parse_args(a: float, b: float) -> tuple[float, float]:
    if b == 2:
        b = 3
    return (a, b)


if __name__ == "__main__":
    import sys

    import pandas as pd

    # import time
    # import debugpy

    print(sys.argv)

    """
        for k in range(0, 1000):
            time.sleep(1)
            print(k)
    """

    dc = {"a": range(0, 20)}
    dc = {"a": range(0, 30)}

    df = pd.DataFrame({"a": dc.values()})

    """
        debugpy.listen(5678)
        print("Waiting for debugger attach")
        debugpy.wait_for_client()
    debugpy.breakpoint()
    """

    print(f"sum_(1, 1) = {sum_(1, 1)}")
    print(f"sum_(2, 1) = {sum_(2, 1)}")
    print(f"sum_(2, 2) = {sum_(2, 2)}")

    # for post-mortem debugging
    sum_(2, "a")
