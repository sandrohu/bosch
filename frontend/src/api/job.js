import request from './index'

// 职位相关API
export const jobAPI = {
  // 获取职位列表
  getJobs(params) {
    return request.get('/jobs', { params })
  },

  // 获取职位详情
  getJobDetail(id) {
    return request.get(`/jobs/${id}`)
  },

  // 创建职位
  createJob(data) {
    return request.post('/jobs', data)
  },

  // 更新职位
  updateJob(id, data) {
    return request.put(`/jobs/${id}`, data)
  },

  // 删除职位
  deleteJob(id) {
    return request.delete(`/jobs/${id}`)
  },

  // 投递简历
  applyJob(jobId, data) {
    return request.post(`/jobs/${jobId}/apply`, data)
  }
}