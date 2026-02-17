from fastapi import APIRouter, UploadFile, File
from app.services.image_service import save_image
from app.services.detection_service import detect_objects
from app.services.caption_service import generate_caption

router = APIRouter()

@router.post("/generate-ad/")
async def generate_ad(file: UploadFile = File(...)):

    # Save image
    image_path = await save_image(file)

    # Detect product
    detected = detect_objects(image_path)

    # Generate caption
    caption = generate_caption(image_path)

    return {
        "detected_objects": detected,
        "caption": caption
    }
