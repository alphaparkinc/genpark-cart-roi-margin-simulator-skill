class CartROIMarginSimulatorClient:
    def simulate(self, revenue: float, cost: float) -> dict:
        return {"roi_ratio": round(revenue / max(1.0, cost), 2)}