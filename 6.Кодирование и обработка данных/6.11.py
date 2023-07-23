from struct import Struct
def write_records(records,format,f):
    '''
    Записывает последовательность кортежей в бинарный файл структур.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))
if __name__ == '__main__':
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]
with open('data.b','wb') as file:
    write_records(records,'<idd',file)
#want to read the whole file
def unpack_records(format,data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data,offset)
        for offset in range(0,len(data),record_struct.size))
if __name__ == '__main__':
    with open('data.b','rb') as file:
        data = file.read()
    for rec in unpack_records('<idd',data):
        print(rec)
