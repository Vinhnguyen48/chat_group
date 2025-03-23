from sqlalchemy import create_engine, text

# Thông tin kết nối MySQL
MYSQL_USER = "root"  
MYSQL_PASSWORD = "hide"  
MYSQL_HOST = "localhost"  
MYSQL_PORT = "3306"  
MYSQL_DB = "chat_group"  

# Tạo chuỗi kết nối MySQL
DATABASE_URI = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"

def test_mysql_connection():
    try:
        # Tạo engine kết nối
        engine = create_engine(DATABASE_URI)
        
        # Mở kết nối
        with engine.connect() as connection:
            result = connection.execute(text("SELECT VERSION();"))  # ✅ Sửa lỗi tại đây
            version = result.scalar()  # Lấy phiên bản MySQL
            print(f" Kết nối MySQL thành công! Phiên bản: {version}")
    
    except Exception as e:
        print(f" Lỗi kết nối MySQL: {e}")

if __name__ == "__main__":
    test_mysql_connection()
