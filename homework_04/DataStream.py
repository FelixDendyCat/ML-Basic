from DataDescriptor import BaseDataDescriptor, OSDataDescriptor

class BaseDataStream:
    # можно кидать исключения вместо bool
    def reserve_data(self, data_descriptor: BaseDataDescriptor)->bool:
        pass
    def get_data(self, data_descriptor: BaseDataDescriptor)->bool:
        pass
    def update_data(self, data_descriptor: BaseDataDescriptor)->bool:
        pass
