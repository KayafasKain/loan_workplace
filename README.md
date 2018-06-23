# Loan workplace(WIP)
##### Managing loans

Даное приложение предназначено для выдачи, управления и оценки займов.

### Функционал:

* Оценка платежеспособности клиента (WIP)
* Выдача займов (WIP)
* Мониторинг выданых займов (WIP)

### API (WIP)
#### Loans
 * GET loans
 * GET loans/order/<str: "amount/date/interest">
 * GET loans/avg/<str: "amount/interest">
 * GET loans/expired
 * GET loans/paid
 * GET loans/by_status_id/<int:id>
 * GET loans/by_type_id/<int:id>
 * GET loans/by_profile_id/<int:id>
 * GET loans/by_type_id/<int:id>
 * GET loans/loan/<int:id>
 * GET loans/types/
 * GET loans/types/type/<int:id>
 * GET loans/statuses/
 * GET loans/statuses/status/<int:id>
 
#### Profiles
 * GET profiles
 * GET profiles/order/<str: "income/age/last_loan/last_paid/last_updated">
 * GET profiles/profile/avg/<int:id>/<str: "income/loan_count/loan_value">
 * GET profiles/profile/loans/<int:id>/<str: "/expired/paid/all">
 * GET profiles/profile/by_employment_type_id/<int:id>
 * GET profiles/profile/by_client_class_id/<int:id>
 * GET profiles/client_classes/
 * GET profiles/client_classes/class/<int:id>
 * GET profiles/employment_types/
 * GET profiles/employment_types/type/<int:id>
