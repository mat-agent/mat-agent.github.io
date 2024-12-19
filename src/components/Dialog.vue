<template>
  <div class="dialog-card">
    <el-card>
      <div class="dialog-bg">
        <div class="question"><b>Question: </b><br>{{ data.question.value }}</div>
        <el-image class="dialog-image" :src="'./data/demodata/' + data.image" fit="contain"></el-image>
        <div class="dialog-tags">
          <el-tag type="warning">{{ data.source }}</el-tag>
        </div>
      </div>
      <div v-for="c in data.conversations" :class="{ message: true, 'message-right': c.role === 'student' }">
        <div class="user-icon">
          <template v-if="c.role === 'teacher'">
            <el-avatar src="./teacher.png" shape="square" />
          </template>
          <template v-else>
            <el-avatar src="./student.png" shape="square" />
          </template>
        </div>
        <div class="message-bubble">
          {{ c.value }}
        </div>
      </div>
    </el-card>
  </div>
</template>

<script setup>
const props = defineProps(['data'])
</script>

<style scoped>
.dialog-card {
  max-width: 100%;
}

.dialog-bg {
  background-color: #eee;
  border-radius: 4px;
  padding: 10px;
}

.dialog-tags {
  text-align: left;
}

.dialog-image {
  width: 100%;
  height: 200px;
  border-radius: 4px;
}

.question {
  color: #666;
  text-align: left;
  margin-bottom: 10px;
}

.message {
  display: flex;
  margin: 20px 0 20px 0;
}

.message-right {
  flex-direction: row-reverse;
}

.message-right .message-bubble {
  background-color: #d9ecff;
}

.user-icon {
  width: 64px;
}

.message-bubble {
  text-align: left;
  padding: 10px;
  background-color: #eee;
  border-radius: 4px;
  max-width: 80%;
  background-color: #fde2e2;
}
</style>
