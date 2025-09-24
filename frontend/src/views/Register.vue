<template>
  <div class="register-container">
    <div class="register-form">
      <h2>用户注册</h2>
      <form @submit.prevent="handleRegister">
        <div class="form-item">
          <input
            v-model="registerForm.username"
            type="text"
            placeholder="请输入用户名"
            required
          />
        </div>
        <div class="form-item">
          <input
            v-model="registerForm.email"
            type="email"
            placeholder="请输入邮箱"
            required
          />
        </div>
        <div class="form-item">
          <input
            v-model="registerForm.password"
            type="password"
            placeholder="请输入密码"
            required
          />
        </div>
        <div class="form-item">
          <input
            v-model="registerForm.confirmPassword"
            type="password"
            placeholder="请确认密码"
            required
          />
        </div>
        <div class="form-item">
          <select v-model="registerForm.userType">
            <option value="jobseeker">求职者</option>
            <option value="company">企业用户</option>
          </select>
        </div>
        <div class="form-item">
          <button type="submit">注册</button>
        </div>
        <div class="form-footer">
          <router-link to="/login">已有账号？立即登录</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { authAPI } from '../api/auth'

const router = useRouter()
const registerForm = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: '',
  userType: 'jobseeker'
})

const handleRegister = async () => {
  // TODO: 实现注册逻辑
  if (registerForm.value.password !== registerForm.value.confirmPassword) {
    alert('两次输入的密码不一致')
    return
  }
  console.log('注册表单数据:', registerForm.value)
  alert('注册功能待实现')
}
</script>

<style scoped>
.register-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  background: #f5f5f5;
}

.register-form {
  background: white;
  padding: 40px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
  width: 100%;
  max-width: 400px;
}

h2 {
  text-align: center;
  margin-bottom: 30px;
  color: #333;
}

.form-item {
  margin-bottom: 20px;
}

input, select {
  width: 100%;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
  font-size: 14px;
}

button {
  width: 100%;
  padding: 12px;
  background: #409eff;
  color: white;
  border: none;
  border-radius: 4px;
  font-size: 16px;
  cursor: pointer;
}

button:hover {
  background: #66b1ff;
}

.form-footer {
  text-align: center;
  margin-top: 20px;
}

.form-footer a {
  color: #409eff;
  text-decoration: none;
  font-size: 14px;
}
</style>