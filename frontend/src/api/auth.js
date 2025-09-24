import request from './index'

// 用户认证相关API
export const authAPI = {
  // 登录
  login(data) {
    return request.post('/auth/login', data)
  },

  // 注册
  register(data) {
    return request.post('/auth/register', data)
  },

  // 获取当前用户信息
  getCurrentUser() {
    return request.get('/auth/user')
  },

  // 登出
  logout() {
    return request.post('/auth/logout')
  }
}