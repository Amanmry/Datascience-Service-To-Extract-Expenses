from typing import Optional;
from langchain_core.pydantic_v1 import BaseModel;
from langchain_core.pydantic_v1 import Field;


class Expense(BaseModel):
        """Information about a transaction made on any Card"""
        amount: Optional[str] = Field(title = "expense", description = "Expense made in transaction")
        merchant: Optional[str] = Field(title = "merchant", description = "Merchent name whome the transaction has been made")
        currency: Optional[str] = Field(title = "currency", description = "Currency of transaction")

