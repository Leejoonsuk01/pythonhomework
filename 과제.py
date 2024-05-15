
def calculate_incident_rate(number_of_incidents, number_of_employees, hours_per_week, weeks_per_year):
    # 노출 시간 계산
    exposure_hours = number_of_employees * hours_per_week * weeks_per_year
    # 재해율 계산
    incident_rate = (number_of_incidents / exposure_hours) * 200000
    return incident_rate, exposure_hours

def calculate_total_cost(direct_costs, indirect_multiplier=4):
    # 총 재해 비용 계산
    indirect_costs = direct_costs * indirect_multiplier
    total_costs = direct_costs + indirect_costs
    return total_costs / 10000  # 원에서 만원 단위로 변경

def suggest_safety_measures(incident_rate):
    # 안전 개선 조치 제안
    if incident_rate < 0.5:
        return "현재 안전 관리가 잘 이루어지고 있습니다. 지속적인 모니터링과 기존 안전 프로그램 유지가 필요합니다."
    elif 0.5 <= incident_rate < 2.0:
        return "경미한 안전 문제가 있습니다. 위험 요소를 식별하고 개선하기 위한 안전 교육 및 작업장 환경 개선이 필요합니다."
    else:
        return "심각한 안전 문제가 있습니다. 즉각적인 개선 조치와 안전 프로그램 강화가 필요합니다."

def calculate_expected_savings(incident_rate, total_costs, expected_reduction_rate):
    # 기대 효과 계산
    expected_incident_rate = incident_rate * (1 - expected_reduction_rate)
    expected_savings = total_costs * expected_reduction_rate
    return expected_incident_rate, expected_savings

def get_float_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return float(user_input)
        except ValueError:
            print("입력이 잘못되었습니다. 숫자를 입력해주세요.")

def get_int_input(prompt):
    while True:
        user_input = input(prompt)
        try:
            return int(user_input)
        except ValueError:
            print("입력이 잘못되었습니다. 정수를 입력해주세요.")

def main():
    while True:
        # 사용자 입력 받기
        number_of_incidents = get_float_input("재해 건수를 입력하세요 (건): ")
        number_of_employees = get_int_input("근로자 수를 입력하세요 (명): ")
        hours_per_week = get_int_input("주당 근무 시간을 입력하세요: ")
        weeks_per_year = get_int_input("연간 근무 주 수를 입력하세요: ")
        direct_costs = get_float_input("직접 비용을 입력하세요 (원): ")
        indirect_multiplier = get_float_input("간접 비용 배율을 입력하세요 (예: 1, 2, 3, 4): ")
        expected_reduction_rate = get_float_input("기대하는 재해율 감소율을 입력하세요 (예: 0.1, 0.2, 0.3): ")

        # 재해율 및 노출 시간 계산
        incident_rate, exposure_hours = calculate_incident_rate(number_of_incidents, number_of_employees, hours_per_week, weeks_per_year)

        # 재해 총 비용 계산 (만원 단위)
        total_costs = calculate_total_cost(direct_costs, indirect_multiplier)

        # 안전 개선 조치 제안
        safety_measures = suggest_safety_measures(incident_rate)

        # 기대 효과 계산 (만원 단위)
        expected_incident_rate, expected_savings = calculate_expected_savings(incident_rate, total_costs, expected_reduction_rate)

        # 결과 출력
        print(f"\n노출 시간: {exposure_hours} 시간")
        print(f"계산된 재해율: {incident_rate:.2f} (백만 시간당 재해 건수)")
        print(f"계산된 총 재해 비용: {total_costs:.2f}만원")
        print(f"제안된 안전 개선 조치: {safety_measures}")
        print(f"기대되는 새로운 재해율: {expected_incident_rate:.2f} (백만 시간당 재해 건수)")
        print(f"기대되는 경제적 이익: {expected_savings:.2f}만원\n")

        # 사용자에게 반복 여부를 묻기
        continue_calculating = input("더 많은 데이터로 계산을 계속하시겠습니까? (yes/no): ").strip().lower()
        if continue_calculating != 'yes':
            break

if __name__ == "__main__":
    main()