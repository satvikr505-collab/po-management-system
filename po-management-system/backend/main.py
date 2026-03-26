from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from backend import models, schemas
from backend.database import engine, SessionLocal

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# DB connection
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Test route
@app.get("/")
def home():
    return {"message": "API is running"}


# ---------------- VENDOR ----------------
@app.post("/vendors")
def create_vendor(name: str, contact: str, rating: int, db: Session = Depends(get_db)):
    vendor = models.Vendor(name=name, contact=contact, rating=rating)
    db.add(vendor)
    db.commit()
    return {"message": "Vendor created"}


# ---------------- PRODUCT ----------------
@app.post("/products")
def create_product(name: str, sku: str, unit_price: float, stock_level: int, db: Session = Depends(get_db)):
    product = models.Product(
        name=name,
        sku=sku,
        unit_price=unit_price,
        stock_level=stock_level
    )
    db.add(product)
    db.commit()
    return {"message": "Product created"}


# ---------------- PURCHASE ORDER ----------------
@app.post("/purchase-orders")
def create_purchase_order(po: schemas.PurchaseOrderCreate, db: Session = Depends(get_db)):
    total = 0

    for item in po.items:
        total += item.price * item.quantity

    tax = total * 0.05
    final_total = total + tax

    po_db = models.PurchaseOrder(
        reference_no="PO001",
        vendor_id=po.vendor_id,
        total_amount=final_total,
        status="Created"
    )

    db.add(po_db)
    db.comm()

    return {"total": final_total}