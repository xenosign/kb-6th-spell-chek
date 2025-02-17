import pdfplumber
import os

def extract_text_pdfplumber(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text()            
    return text

def convert_pdfs_to_txt(folder_path):
    # 폴더 내의 모든 파일 목록 가져오기
    files = os.listdir(folder_path)
    
    # PDF 파일만 필터링
    pdf_files = [f for f in files if f.lower().endswith('.pdf')]
    
    # 각 PDF 파일에 대해 처리
    for pdf_file in pdf_files:
        # PDF 파일의 전체 경로
        pdf_path = os.path.join(folder_path, pdf_file)
        
        # 결과 txt 파일명 생성 (확장자만 변경)
        txt_filename = os.path.splitext(pdf_file)[0] + '.txt'
        
        try:
            # PDF 텍스트 추출
            text = extract_text_pdfplumber(pdf_path)
            
            # txt 파일로 저장
            with open(txt_filename, "w", encoding="utf-8") as f:
                f.write(text)
            
            print(f"변환 완료: {pdf_file} -> {txt_filename}")
            
        except Exception as e:
            print(f"오류 발생 ({pdf_file}): {str(e)}")

# 사용 예시
folder_path = "D:/spell-check/front/01"
convert_pdfs_to_txt(folder_path)