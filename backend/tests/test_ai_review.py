from app.services.ai_review_service import AIReviewService

result = AIReviewService.review(".")

print(result["review"])