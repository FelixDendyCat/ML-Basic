# базовый класс описателя блока данных (полный путь, ID либо адрес в облаке)
class BaseDataDescriptor:
    size:int

class OSDataDescriptor (BaseDataDescriptor):
    file_path:str