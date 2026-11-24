def calculate_sla_metrics(total_minutes: int, downtime_minutes: float, target_sla: float = 99.9) -> dict:
    uptime_pct = ((total_minutes - downtime_minutes) / total_minutes) * 100
    allowed_downtime = total_minutes * (1 - target_sla / 100)
    remaining_budget = round(allowed_downtime - downtime_minutes, 2)
    return {
        "actual_uptime_pct": round(uptime_pct, 4),
        "allowed_downtime_mins": round(allowed_downtime, 2),
        "remaining_error_budget_mins": remaining_budget,
        "sla_breached": remaining_budget < 0
    }

if __name__ == "__main__":
    # 30-day month = 43,200 minutes
    print(calculate_sla_metrics(43200, 18.5, target_sla=99.9))
