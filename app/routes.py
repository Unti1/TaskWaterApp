from fastapi import APIRouter, HTTPException
from .models import Store, Item
from .schemas import Operation, GroupOperation, StoreReport
from fastapi.responses import FileResponse
import pandas as pd

router = APIRouter()

@router.get("/stores/{store_id}", response_model=StoreReport)
async def get_store(store_id: str):
    store = Store.get_store(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store

@router.get("/stores/{store_id}/xlsx_report")
async def get_xlsx_report(store_id: str):
    store = Store.get_store(store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    
    df = pd.DataFrame(store['report'])
    file_path = f"/tmp/{store_id}_report.xlsx"
    df.to_excel(file_path, index=False)
    return FileResponse(file_path, media_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet', filename=f"{store_id}_report.xlsx")

@router.post("/stores/{store_id}")
async def post_store_operation(store_id: str, operation: Operation):
    store = Store.get_store(store_id)
    if not store:
        Store.create_store(store_id)
        store = Store.get_store(store_id)
    
    item = Item.get_item(operation.item_id)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")

    if operation.operation == 'demand':
        new_quantity = item['quantity'] - operation.quantity
    else:  # 'supply'
        new_quantity = item['quantity'] + operation.quantity

    if new_quantity < 0:
        raise HTTPException(status_code=400, detail="Not enough items in stock")

    Item.update_item(operation.item_id, new_quantity)

    for rep in store['report']:
        if rep['item_id'] == operation.item_id:
            rep['quantity'] = new_quantity
            break
    else:
        store['report'].append({'item_id': operation.item_id, 'quantity': new_quantity})

    Store.update_store(store_id, store['report'])
    return {"store": store}

@router.post("/stores/{store_id}/group_op")
async def post_store_group_operation(store_id: str, group_operation: GroupOperation):
    store = Store.get_store(store_id)
    if not store:
        Store.create_store(store_id)
        store = Store.get_store(store_id)

    for operation in group_operation.items:
        item = Item.get_item(operation.item_id)
        if not item:
            raise HTTPException(status_code=404, detail=f"Item {operation.item_id} not found")

        if group_operation.operation == 'demand':
            new_quantity = item['quantity'] - operation.quantity
        else:  # 'supply'
            new_quantity = item['quantity'] + operation.quantity

        if new_quantity < 0:
            raise HTTPException(status_code=400, detail=f"Not enough items in stock for {operation.item_id}")

        Item.update_item(operation.item_id, new_quantity)

        for rep in store['report']:
            if rep['item_id'] == operation.item_id:
                rep['quantity'] = new_quantity
                break
        else:
            store['report'].append({'item_id': operation.item_id, 'quantity': new_quantity})

    Store.update_store(store_id, store['report'])
    return {"store": store}

@router.post("/stores/{store_id}/clean")
async def post_store_clean(store_id: str):
    Store.update_store(store_id, [])
    return {"store": Store.get_store(store_id)}
