'''
Модуль для наождения нужного аргумента в функции
'''

from inspect import signature

class argument_parsing_obj:
    def __init__(self, func, args, kwargs):
        self.parameters = list(signature(func).parameters)
        self.args = args
        self.kwargs = kwargs

    async def get_default(self):
        code = self.func.__code__
        arg_names = code.co_varnames[:code.co_argcount]
        defaults = self.func.__defaults__ or ()
        default_args = dict(zip(arg_names[-len(defaults):], defaults))
        default_args.update(self.kwargs)
        return default_args

    async def argument_parsing_name(self, name_arg):
        if name_arg not in self.parameters:
            return None
        parametr_index = self.parameters.index(name_arg)
        if parametr_index <= len(self.args)-1:
            return self.args[parametr_index]
        else:
            return await self.get_default()[name_arg]