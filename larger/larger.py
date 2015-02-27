import inspect
import types

from decorator import decorator


@decorator
def larger(___f, *args, **kwargs):
    """Lazily evaluate function arguments."""

    cache = {}
    resolved_args = []

    for name, arg in zip(inspect.getargspec(___f).args, args):
        # evaluate lambda arguments
        if isinstance(arg, types.LambdaType):
            try:
                val_args = [cache[k] for k in inspect.getargspec(arg).args]
            except KeyError as e:
                raise ValueError(
                    "Unable to resolve input for '{}': {}".format(name, e)
                )
            arg = arg(*val_args)

        resolved_args.append(arg)
        cache[name] = arg

    return ___f(*resolved_args, **kwargs)
