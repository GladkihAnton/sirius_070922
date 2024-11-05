from prometheus_client import Counter, Histogram

BUCKETS = [
    0.25,
    0.5,
    0.75,
    1,
    float('+inf'),
]

LATENCY = Histogram(
    "latency_seconds",
    "Number of seconds",
    labelnames=['handler'],
    buckets=BUCKETS,
)

TOTAL_REQ = Counter(
    'counter_handler',
    'Считает то-то',
    labelnames=['handler']
)
TOTAL_REQ_WITH_STATUS_CODE = Counter(
    'counter_handler1',
    'Считает то-то',
    labelnames=['handler', 'status_code']
)

TOTAL_REQ.labels('handler1').inc()
TOTAL_REQ_WITH_STATUS_CODE.labels('handler1', 500).inc()
TOTAL_REQ_WITH_STATUS_CODE.labels('handler1', 200).inc()
