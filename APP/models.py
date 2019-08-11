from datetime import datetime

from APP import db

# 用户名 手机 设备名 密码
class User(db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    phone = db.Column(db.String(11), unique=True)
    addTime = db.Column(db.DateTime, index=True, default=datetime.now())
    userlogs = db.relationship('Userlog', backref='user')  # 关联  外键关系关联

    def __repr__(self):
        return "<user %r>" % self.name

# 会员登录日迹
class Userlog(db.Model):
    __tablename__ = "userlog"
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    ip = db.Column(db.String(100))
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)
    phone = db.Column(db.String(11), unique=True)
    info = db.Column(db.Text)
    face = db.Column(db.String(255), unique=True)

    uuid = db.Column(db.String(255), unique=True)

    def __repr__(self):
        return "<Userlog %r>" % self.id
# 管理员
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 编号
    name = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    is_super = db.Column(db.SmallInteger)
    role_id = db.Column(db.Integer, db.ForeignKey('role.id'))
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)
    adminlogs = db.relationship("Adminlog", backref='admin')
    adminsoplog = db.relationship("Oplog", backref='admin')

    def __repr__(self):
        return "<Admin %r>" % self.name

    def check_pwd(self, pwd):
        from werkzeug.security import check_password_hash
        return check_password_hash(self.password, pwd)

# 管理员登录日志
class Adminlog(db.Model):
    __tablename__ = "adminlog"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    addTime = db.Column(db.DateTime, index=True, default=datetime.now)

    def __repr__(self):
        return "<Adminlog %r>" % self.id

# 操作日志
class Oplog(db.Model):
    __tablename__ = "oplog"
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'))
    ip = db.Column(db.String(100))
    reason = db.Column(db.String(600))
    addTime = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<Oplog %r>" % self.id

# 产品
class Productstyle(db.Model):
    __tablename__ = "productstyle"
    id = db.Column(db.Integer, primary_key=True)
    style = db.Column(db.String(100), unique=True)
    info = info = db.Column(db.Text)
    price = db.Column(db.Integer)
    face = db.Column(db.String(255), unique=True)
    reason = db.Column(db.String(600))
    addTime = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<Productstyle %r>" % self.id

#CPR成绩
# 模式 分数 操作时间
# 按压总数  按压正确 按压错误  过大 过小 位置 多按 少按 实时频率 平均频率
# 吹气总数 吹气正确 吹气错误   过大 过小 气道 多吹 少吹
class CPRGrade(db.Model):
    __tablename__ = "cprgrade"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100))
    number = db.Column(db.String(255), unique=True)
    mode=db.Column(db.String(255))

    operatortime = db.Column(db.Integer)
    pressall = db.Column(db.Integer)
    presstrue = db.Column(db.Integer)
    presserror = db.Column(db.Integer)
    pressbig = db.Column(db.Integer)
    presssmall = db.Column(db.Integer)
    pressposition = db.Column(db.Integer)
    pressunder = db.Column(db.Integer)
    presssubpass = db.Column(db.Integer)
    pressrealreate=db.Column(db.Integer)
    pressavrate = db.Column(db.Integer)

    blowall = db.Column(db.Integer)
    blowtrue=db.Column(db.Integer)
    blowerror=db.Column(db.Integer)
    blowbig=db.Column(db.Integer)
    blowsmall=db.Column(db.Integer)
    blowair=db.Column(db.Integer)
    blowsubpass=db.Column(db.Integer)
    blowunder=db.Column(db.Integer)

    addTime = db.Column(db.DateTime, index=True, default=datetime.now())

    def __repr__(self):
        return "<cprgrade %r>" % self.id