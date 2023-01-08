from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/products",
                    tags=["Products"])

class Product(BaseModel):
    id: int
    name: str
    price: float

product_list = [Product(id=1, name="TV", price=999.90),
              Product(id=2, name="Radio", price=500.90),
              Product(id=3, name="Telefono", price=1200.00),
              Product(id=4, name="Cargador Telefono", price=40.00),]

@router.get("/", response_model=list[Product])
async def products():
    """
    Lista a todos los productos
    """
    return product_list

# Path
@router.get("/{id}", response_model=Product)
async def product(id: int):
    """
    Busca producto por Id
    """
    return search_product(id)

# util
def search_product(id: int):
    """
    Busca un producto por el ID
    """
    products = filter(lambda product: product.id == id, product_list)
    try:
        return list(products)[0]
    except:
        raise HTTPException(status_code=404, detail="producto no existe")