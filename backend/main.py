from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import pykakasi
from googletrans import Translator
import logging

# ロギング設定
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# FastAPIアプリケーションの初期化
app = FastAPI(
    title="翻訳・カタカナ変換API",
    description="外国語を日本語に翻訳し、その発音をカタカナに変換するAPIです",
    version="1.0.0"
)

# CORS設定（フロントエンドからのリクエストを許可）
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 本番環境では特定のオリジンのみに制限すべき
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# リクエストモデル
class TranslationRequest(BaseModel):
    text: str
    source_language: Optional[str] = "auto"

# レスポンスモデル
class TranslationResponse(BaseModel):
    original_text: str
    source_language: str
    translated_text: str
    katakana: str

# 翻訳機能
def translate_to_japanese(text: str, source_lang: str = "auto"):
    try:
        translator = Translator()
        result = translator.translate(text, src=source_lang, dest="ja")
        return {
            "translated_text": result.text,
            "source_language": result.src
        }
    except Exception as e:
        logger.error(f"翻訳エラー: {str(e)}")
        raise HTTPException(status_code=500, detail=f"翻訳処理中にエラーが発生しました: {str(e)}")

# カタカナ変換機能
def convert_to_katakana(text: str):
    try:
        kks = pykakasi.kakasi()
        result = kks.convert(text)
        return "".join([item['kana'] for item in result])
    except Exception as e:
        logger.error(f"カタカナ変換エラー: {str(e)}")
        raise HTTPException(status_code=500, detail=f"カタカナ変換中にエラーが発生しました: {str(e)}")

# ルート
@app.get("/")
def read_root():
    return {"message": "翻訳・カタカナ変換APIへようこそ！"}

# 翻訳・カタカナ変換エンドポイント
@app.post("/translate", response_model=TranslationResponse)
def translate_and_convert(request: TranslationRequest):
    # 入力テキストのバリデーション
    if not request.text or len(request.text.strip()) == 0:
        raise HTTPException(status_code=400, detail="テキストが入力されていません")
    
    # 翻訳実行
    logger.info(f"リクエスト: {request.text}, 言語: {request.source_language}")
    translation_result = translate_to_japanese(request.text, request.source_language)
    
    # カタカナ変換
    katakana = convert_to_katakana(translation_result["translated_text"])
    
    # レスポンス作成
    return TranslationResponse(
        original_text=request.text,
        source_language=translation_result["source_language"],
        translated_text=translation_result["translated_text"],
        katakana=katakana
    )

# サーバー起動設定
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True) 