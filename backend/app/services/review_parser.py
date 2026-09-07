import json

from fastapi import HTTPException


class ReviewParser:

    REQUIRED_FIELDS = {
        "overall_score",
        "strengths",
        "issues",
        "recommendations",
    }

    @classmethod
    def parse(cls, review: str):

        review = review.strip()

        if review.startswith("```json"):
            review = review[7:]

        if review.endswith("```"):
            review = review[:-3]

        review = review.strip()

        try:

            result = json.loads(review)

        except json.JSONDecodeError:

            raise HTTPException(
                status_code=500,
                detail="AI returned invalid JSON.",
            )

        missing = cls.REQUIRED_FIELDS - result.keys()

        if missing:

            raise HTTPException(
                status_code=500,
                detail=f"AI response missing fields: {', '.join(sorted(missing))}",
            )

        return result