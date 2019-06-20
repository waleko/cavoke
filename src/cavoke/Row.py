from abc import abstractmethod

from .Unit import Unit


class Row(Unit, list):
    def __genSub(self, BaseClass: type, w, h, name, *baseArgs):
        res = BaseClass(*baseArgs)
        res.w = w
        res.h = h
        res.name = name
        return res

    def __init__(self, items_x: int, BaseClass: type,
                 name: str = "", w=600, h=600, initPayload: dict = {},
                 *baseArgs):
        super().__init__(name, w, h, initPayload)
        self.items_x = items_x
        self.__units = [self.__genSub(BaseClass, w // items_x, h, name + '_' + str(i),
                                      *baseArgs) for i in range(items_x)]
        self.__BaseClass = BaseClass
        self.isHorizontal = True

    def __getitem__(self, item):
        return self.__units.__getitem__(item)

    def __iter__(self):
        for i in range(self.items_x):
            yield self.__units[i]

    def getDisplayDict(self) -> list:
        return self.__units

    def click(self):
        pass

    def drag(self, toUnit):
        pass