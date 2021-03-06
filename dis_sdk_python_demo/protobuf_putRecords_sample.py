#!/usr/bin/python
# -*- coding:utf-8 -*-
from dis_sdk_python import *

streamname = "dis_test1"

def protobuf_putRecords_test():
    cli = disclient(endpoint='', ak='', sk='', projectid='', region='',bodySerializeType='protobuf')

    records = []
    record1={"data": "xxxxx", "partition_key": '0'}
    record2 = {"data": "xxxxx", "partition_key": '0'}
    records.append(record1)
    records.append(record2)

    try:
        r = cli.putRecords(streamname,records)
        print(r.statusCode)
        # print(r.recordResult)
        try:
            print(json.dumps(r.body))
        except:
            print(r.body)
        # for i in r.getSendRecordResult(r.recordResult):
        #     print("%s %s %s %s" % (i.partition_id,i.sequence_number,i.error_code, i.error_message))

    except Exception as ex:
        print(ex)




if __name__ == '__main__':
    print("Use your Stream to protobuf_putRecords")
    protobuf_putRecords_test()



