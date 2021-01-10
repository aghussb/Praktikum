import json


class module:

    def __init__(self, props):
        self.open_json = open('data.json', )
        self.json_file = json.load(self.open_json)
        self.props_json = props

    def authSave(self, data):
        self.json_file[self.props_json].append(data)
        for propsData in self.json_file:
            if propsData == self.props_json:
                self.json_file[self.props_json] = self.json_file[self.props_json]

        with open('data.json', 'w') as outfile:
            json.dump(self.json_file, outfile)

        self.open_json.close()

        return 'Sukses Registrasi'

    def deleteData(self, index):
        del self.json_file[self.props_json][index - 1]
        with open('data.json', 'w') as outfile:
            json.dump(self.json_file, outfile)

        self.open_json.close()
        return "Sukses Delete Data"

    def saveData(self, data, status, index):
        if status == 1:
            self.json_file[self.props_json].append(data)
            for propsData in self.json_file:
                if propsData == self.props_json:
                    self.json_file[self.props_json] = self.json_file[self.props_json]

            pesan = 'Sukses Tambah Data'
        else:
            self.json_file[self.props_json][index - 1]['nama'] = self.json_file[self.props_json][index - 1]['nama']
            for props in data:
                self.json_file[self.props_json][index - 1][props] = data[props]
            pesan = 'Sukses Update Data'

        with open('data.json', 'w') as outfile:
            json.dump(self.json_file, outfile)

        self.open_json.close()
        return pesan

    def dataRead(self):
        return self.json_file[self.props_json]

    def simpanBelanja(self, dataPembeli, tunai, tanggal, waktu):
        dictionaryLaporan = {
            "tanggal": tanggal,
            "waktu": waktu,
            "tunai": tunai,
            "data": dataPembeli
        }
        self.json_file['laporan'].append(dictionaryLaporan)
        for item in dataPembeli:
            self.json_file[self.props_json][item['id']]['stock'] = self.json_file[self.props_json][item['id']][
                                                                       'stock'] - item['stock']

        with open('data.json', 'w') as outfile:
            json.dump(self.json_file, outfile)

        self.open_json.close()
        return 'Sukses Simpan Belanja'
