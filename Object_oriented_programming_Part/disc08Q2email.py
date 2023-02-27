# write three different classes, Mailman, Client, and Email to simulate email
class Email:
    """Every email object has 3 instance attributes: the
    message, the sender name, and the recipient name.
    """
    def __init__(self, msg, sender_name, recipient_name):
        self.msg = msg#信件内容
        self.sender_name = sender_name#发件人名字
        self.recipient_name = recipient_name#收信人名字
class Mailman:#邮差应该是
    """Each Mailman has an instance attribute clients, which
    is a dictionary that associates client names with
    client objects. #类属性，clients，dict类型，关联客户名字和客户对象
    """
    def __init__(self):
        self.clients = {}
    def send(self, email):
        """Take an email and put it in the inbox of the client
        it is addressed to.投到客户的邮件地址收件箱
        """
        self.clients[email.recipient_name].receive(email)

    def register_client(self, client, client_name):
        """Takes a client object and client_name and adds it
        to the clients instance attribute.#客户对象，客户名字，添加到clients实例属性
        """#应用字典，call参数
        self.clients[client_name] = client

class Client:#客户
    """Every Client has instance attributes name (which is
    used for addressing emails to the client), mailman
    (which is used to send emails out to other clients), and
    inbox (a list of all emails the client has received).
    """#实例属性，确定地址，邮寄人，投递箱子
    def __init__(self, mailman, name):
        self.inbox = []
        self.mailman = mailman
        self.name = name
        #
        self.mailman.register_client(self, self.name)
    def compose(self, msg, recipient_name):
        """Send an email with the given message msg to the
        given recipient client.发msg给recipient_name
        """
        self.mailman.send(Email(msg, self.name, recipient_name))
        
    def receive(self, email):
        """Take an email and add it to the inbox of this
        client.
        """
        self.inbox.append(email)
