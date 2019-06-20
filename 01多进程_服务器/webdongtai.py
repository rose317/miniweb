import socket
import re
import multiprocessing
import time
import miniweb_frame


class WSGIServer(object):
    def __init__(self):
        # 1.创建套接字
        self.tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.tcp_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 2.绑定套接字
        self.tcp_server.bind(("", 7890))
        # 3.将套接字设置成被动
        self.tcp_server.listen(128)
        # 4.等待客户端发送请求

    def service_client(self,new_tcp_server):
        """为客户端返回数据"""
        recv_data = new_tcp_server.recv(1024).decode("utf-8")
        #print(recv_data)
        request_lines = recv_data.splitlines()
        print("")
        print(">" * 20)
        print(request_lines)
        #1.准备给浏览器发送数据 ---header
        # GET /index.html HTTP/1.1
        # get post put del

        file_name = ""
        ret = re.match(r"[^/]+(/[^ ]*)",request_lines[0])
        if ret:
            file_name = ret.group(1)
            # print("*"*50, file_name)
            if file_name == "/":
                file_name = "/index.html"

        #如果不是以.py结尾的就认为是静态资源
        if not file_name.endswith(".py"):
            try:
                f = open("./html" + file_name,"rb")
            except:
                response = "HTTP/1.1 404 NOT FOUND\r\n"
                response += "\r\n"
                response += "------file not found-----"
                new_tcp_server.send(response.encode("utf-8"))
            else:
                file_content = f.read()
                f.close()
                response = "HTTP/1.1 200 OK\r\n"
                response += "\r\n"
                new_tcp_server.send(response.encode("utf-8"))
                new_tcp_server.send(file_content)
        else:
            env = dict()
            env["PATH_INFO"] = file_name
            body = miniweb_frame.application(env,self.set_response)
            header = "HTTP/1.1 %s\r\n" % self.status
            for temp in self.headers:
                header += "%s:%s\r\n" %(temp[0],temp[1])
            header += "\r\n"
            # body = miniweb_frame.login()
            response = header + body
            new_tcp_server.send(response.encode("utf-8"))

        new_tcp_server.close()

    def set_response(self,status,headers):
        self.status = status
        self.headers = [('server','mini_frame v8.8')]
        self.headers += headers



    def run_forever(self):

        while True:
            new_tcp_server,tcp_addr = self.tcp_server.accept()

            #5.给客户端返回数据
            p = multiprocessing.Process(target=self.service_client,args=(new_tcp_server,))
            p.start()
            new_tcp_server.close()
        self.tcp_server.close()

def main():
    wsg = WSGIServer()
    wsg.run_forever()


if __name__ == '__main__':
    main()