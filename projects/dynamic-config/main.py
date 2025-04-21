"""Example."""

import inspect
import tomllib
import benchmarks


def main():
    """Run example."""

    with open("config.toml", "rb") as f:
        data = tomllib.load(f)

    for config in data["benchmark"]:
        # Get the class object from the package using name from TOML config file
        name = config["name"].title()
        bench_class = getattr(benchmarks, name)

        # Inspect parameters of the class constructor to get applicable
        # inputs. Then build dictionary of input parameters using values
        # defined in TOML config file.
        sig = inspect.signature(bench_class)
        kwargs = {k: config[k] for k in sig.parameters if k in config}

        # Create the class instance with the matched args
        b = bench_class(**kwargs)

        print(b)
        print(vars(b), "\n")


if __name__ == "__main__":
    main()
