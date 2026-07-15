class EvaluationEngine:

    def evaluate(self, expected, predicted):

        if expected == predicted:

            return {
                "score": 1.0,
                "passed": True
            }

        return {
            "score": 0.0,
            "passed": False
        }


evaluation_engine = EvaluationEngine()
