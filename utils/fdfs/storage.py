from django.core.files.storage import Storage
from fdfs_client.client import Fdfs_client,get_tracker_conf
from django.conf import settings

class FDFSStorage(Storage):
    def __init__(self,base_url=None):
        if base_url is  None:
            base_url = settings.FDFS_URL
            self.base_url = base_url


    def _open(self, name, mode='rb'):
        pass


    def _save(self,name,content):
        tracker_path = get_tracker_conf('/home/ningxitong/PycharmProjects/dailyfresh/utils/fdfs/client.conf')  # 绝对路径
        client = Fdfs_client(tracker_path)
        res = client.upload_by_buffer(content.read())
        #{
            #'Group name': group_name,
            #'Remote file_id': remote_file_id,
            #'Status': 'Upload successed.',
            #'Local file name': '',
            #'Uploaded size': upload_size,
            #'Storage IP': storage_ip
        #}
        if res.get('Status') != 'Upload successed.':
            raise Exception('上传文件到fdfs失败')
            #失败
        else:
            file_name = res.get('Remote file_id')
            #上传成功
        return file_name.decode()
    #django 判断文件是否已经存在于django服务器（因为已经保存在fdfs，所以直接返回false表示不存在）
    def exists(self, name):
        return False

    # 返回url
    def url(self, name):
        return self.base_url + name




