<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <v-toolbar-title>日本語翻訳・カタカナ変換アプリ</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <v-container>
        <TranslationForm />
      </v-container>
    </v-main>

    <v-footer app color="primary" dark>
      <span>&copy; {{ new Date().getFullYear() }} - 翻訳・カタカナ変換アプリ</span>
    </v-footer>
  </v-app>
</template>

<script>
import TranslationForm from './components/TranslationForm.vue'

export default {
  name: 'App',
  components: {
    TranslationForm
  }
}
</script>

<style>
html, body {
  font-family: 'Noto Sans JP', sans-serif;
}
</style> 