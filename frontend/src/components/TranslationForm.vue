<template>
  <v-card class="mx-auto my-4" max-width="800">
    <v-card-title class="text-center">
      <h1 class="text-h5">外国語を日本語に翻訳して、カタカナ発音を表示</h1>
    </v-card-title>

    <v-card-text>
      <v-form @submit.prevent="translateText">
        <v-row>
          <v-col cols="12">
            <v-select
              v-model="sourceLanguage"
              :items="languageOptions"
              label="元の言語"
              outlined
              dense
            ></v-select>
          </v-col>
          
          <v-col cols="12">
            <v-textarea
              v-model="inputText"
              label="翻訳するテキストを入力してください"
              outlined
              auto-grow
              rows="4"
              counter
              :loading="loading"
              :disabled="loading"
            ></v-textarea>
          </v-col>
          
          <v-col cols="12" class="text-center">
            <v-btn 
              color="primary" 
              :loading="loading" 
              :disabled="!inputText"
              @click="translateText"
              x-large
            >
              翻訳する
            </v-btn>
          </v-col>
        </v-row>
      </v-form>

      <!-- 結果表示セクション -->
      <v-expand-transition>
        <div v-if="result">
          <v-divider class="my-4"></v-divider>
          
          <v-row>
            <v-col cols="12">
              <h2 class="text-h6 mb-2">翻訳結果:</h2>
              <v-card outlined class="pa-3 mb-4">
                <p>{{ result.translated_text }}</p>
              </v-card>
            </v-col>
            
            <v-col cols="12">
              <h2 class="text-h6 mb-2">カタカナ発音:</h2>
              <v-card outlined class="pa-3" color="secondary" dark>
                <p class="text-h5">{{ result.katakana }}</p>
              </v-card>
            </v-col>
            
            <v-col cols="12" class="text-right">
              <p class="text-caption">元の言語: {{ getLanguageName(result.source_language) }}</p>
            </v-col>
          </v-row>
        </div>
      </v-expand-transition>
    </v-card-text>
    
    <v-snackbar
      v-model="errorSnackbar"
      color="error"
      timeout="5000"
    >
      {{ errorMessage }}
      <template v-slot:action="{ attrs }">
        <v-btn
          text
          v-bind="attrs"
          @click="errorSnackbar = false"
        >
          閉じる
        </v-btn>
      </template>
    </v-snackbar>
  </v-card>
</template>

<script>
import axios from 'axios';

export default {
  name: 'TranslationForm',
  
  data() {
    return {
      inputText: '',
      sourceLanguage: 'auto',
      loading: false,
      result: null,
      errorSnackbar: false,
      errorMessage: '',
      languageOptions: [
        { text: '自動検出', value: 'auto' },
        { text: '英語', value: 'en' },
        { text: 'フランス語', value: 'fr' },
        { text: 'ドイツ語', value: 'de' },
        { text: 'スペイン語', value: 'es' },
        { text: 'イタリア語', value: 'it' },
        { text: '中国語', value: 'zh-cn' },
        { text: '韓国語', value: 'ko' },
        { text: 'ロシア語', value: 'ru' },
        { text: 'ポルトガル語', value: 'pt' }
      ],
      languageMap: {
        'auto': '自動検出',
        'en': '英語',
        'fr': 'フランス語',
        'de': 'ドイツ語',
        'es': 'スペイン語',
        'it': 'イタリア語',
        'zh-cn': '中国語',
        'ko': '韓国語',
        'ru': 'ロシア語',
        'pt': 'ポルトガル語',
        'ja': '日本語'
      }
    };
  },
  
  methods: {
    async translateText() {
      if (!this.inputText) return;
      
      this.loading = true;
      this.result = null;
      
      try {
        const response = await axios.post('http://localhost:8000/translate', {
          text: this.inputText,
          source_language: this.sourceLanguage
        });
        
        this.result = response.data;
      } catch (error) {
        console.error('翻訳エラー:', error);
        this.errorMessage = error.response?.data?.detail || 'エラーが発生しました。しばらくしてからもう一度お試しください。';
        this.errorSnackbar = true;
      } finally {
        this.loading = false;
      }
    },
    
    getLanguageName(code) {
      return this.languageMap[code] || code;
    }
  }
};
</script>

<style scoped>
.v-card {
  border-radius: 12px;
}
</style> 