# Utilities
from utilities.io import read_csv_file, read_file


class Report():
    '''Report class'''

    MONTH_MAP = {
        '1': 'January',
        '2': 'February',
        '3': 'March',
        '4': 'April',
        '5': 'May',
        '6': 'June',
        '7': 'July',
        '8': 'August',
        '9': 'September',
        '10': 'October',
        '11': 'November',
        '12': 'December'
    }

    balance = 0
    credit_transactions_count = 0
    debit_transactions_count = 0
    credit_amount = 0
    debit_amount = 0
    montly_reports = {}

    @property
    def avg_credit_amount(self):
        return self.credit_amount / self.credit_transactions_count

    @property
    def avg_debit_amount(self):
        return self.debit_amount / self.debit_transactions_count

    def register_transaction(self, transaction, date):
        '''Register transaction'''
        self.balance += transaction
        if transaction > 0:
            self.credit_amount += transaction
            self.credit_transactions_count += 1
        else:
            self.debit_amount += transaction
            self.debit_transactions_count += 1

        month = date.split('/')[0]
        if month not in self.montly_reports:
            self.montly_reports[month] = {'transactions_count': 0}
        self.montly_reports[month]['transactions_count'] += 1

    def load_from_csv(self, file_name):
        '''Load data'''
        data = read_csv_file(file_name)
        for row in data[1:]:
            self.register_transaction(float(row[2]), row[1])

    def get_monthly_reports(self, format='json'):
        if format == 'json':
            return self.montly_reports
        elif format == 'text':
            return '\n'.join([
                (
                    f'Number of transactions in {self.MONTH_MAP[month]}:'
                    f'{self.montly_reports[month]["transactions_count"]}')
                for month in self.montly_reports])
        elif format == 'html':
            template = read_file('templates/monthly-report.html')
            return '\n'.join([
                template.replace('{{month}}', self.MONTH_MAP[month])
                .replace(
                    '{{transactions_count}}',
                    str(self.montly_reports[month]['transactions_count']))
                for month in self.montly_reports])

    def get_report(self, format='json'):
        '''Get report'''
        if format == 'json':
            return {
                'balance': self.balance,
                'avg_credit_amount': self.avg_credit_amount,
                'avg_debit_amount': self.avg_debit_amount,
                'montly_reports': self.get_monthly_reports(format)}
        elif format == 'text':
            return '\n'.join([
                f'Total balance is {self.balance}',
                f'{self.get_monthly_reports(format)}',
                f'Average debit amount: {self.avg_debit_amount}',
                f'Average credit amount: {self.avg_credit_amount}'])
        elif format == 'html':
            template = read_file('templates/report.html')
            return (
                template.replace('{{balance}}', str(self.balance))
                .replace(
                    '{{monthly_reports}}',
                    str(self.get_monthly_reports(format)))
                .replace('{{avg_credit_amount}}', str(self.avg_credit_amount))
                .replace(
                    '{{avg_debit_amount}}', str(abs(self.avg_debit_amount))))
        else:
            raise NotImplementedError('Format not supported')
