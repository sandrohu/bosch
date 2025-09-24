from extensions import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

# 用户模型
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    user_type = db.Column(db.String(20), default='jobseeker')  # jobseeker, company, admin
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'user_type': self.user_type,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# 公司模型
class Company(db.Model):
    __tablename__ = 'companies'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    logo = db.Column(db.String(500))
    website = db.Column(db.String(200))
    scale = db.Column(db.String(50))  # 公司规模
    industry = db.Column(db.String(100))  # 行业
    address = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 关系
    user = db.relationship('User', backref='company')
    jobs = db.relationship('Job', backref='company', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'logo': self.logo,
            'website': self.website,
            'scale': self.scale,
            'industry': self.industry,
            'address': self.address
        }

# 职位模型
class Job(db.Model):
    __tablename__ = 'jobs'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=False)
    requirements = db.Column(db.Text)
    salary_min = db.Column(db.Integer)
    salary_max = db.Column(db.Integer)
    location = db.Column(db.String(100))
    job_type = db.Column(db.String(50))  # 全职、兼职、实习
    education = db.Column(db.String(50))  # 学历要求
    experience = db.Column(db.String(50))  # 经验要求
    company_id = db.Column(db.Integer, db.ForeignKey('companies.id'))
    status = db.Column(db.String(20), default='active')  # active, closed
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    applications = db.relationship('Application', backref='job', lazy='dynamic')

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'requirements': self.requirements,
            'salary_range': f'{self.salary_min}-{self.salary_max}K' if self.salary_min and self.salary_max else '面议',
            'location': self.location,
            'job_type': self.job_type,
            'education': self.education,
            'experience': self.experience,
            'company': self.company.to_dict() if self.company else None,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

# 申请/投递模型
class Application(db.Model):
    __tablename__ = 'applications'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('jobs.id'))
    resume_url = db.Column(db.String(500))
    cover_letter = db.Column(db.Text)
    status = db.Column(db.String(20), default='pending')  # pending, reviewed, accepted, rejected
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # 关系
    user = db.relationship('User', backref='applications')

    def to_dict(self):
        return {
            'id': self.id,
            'user': self.user.to_dict() if self.user else None,
            'job': self.job.to_dict() if self.job else None,
            'resume_url': self.resume_url,
            'cover_letter': self.cover_letter,
            'status': self.status,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }