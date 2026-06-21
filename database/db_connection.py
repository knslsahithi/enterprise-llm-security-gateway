from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:Sahithi@localhost:5432/llm_security_gateway"

engine = create_engine(DATABASE_URL)