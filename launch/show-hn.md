# Show HN

Post at https://news.ycombinator.com/submit — **Wed ~8–9am US Eastern**.
Set the URL to the repo, paste the body as the first comment.

## Title (≤ 80 chars)

```
Show HN: UniPay UZ – one Python API for Uzbekistan's payment gateways
```

URL: `https://github.com/javlondevv/unipay-uz`

## First comment (the story + the ask for feedback)

```
Hi HN! I'm a backend engineer in Uzbekistan. Every Python project here that
takes payments ends up re-implementing the same integrations against our local
gateways — Payme, Click, Uzum, Paynet, Octo — each with its own auth scheme,
amount units (som vs. tiyin), and webhook/callback contract. I'd written that
glue three times across different jobs, so I extracted it into one library.

UniPay UZ gives you a single, predictable API across all five providers:

    from unipay_uz.gateways.payme import PaymeGateway

    payme = PaymeGateway(payme_id="...", payme_key="...", is_test_mode=True)
    url = payme.create_payment(id="ORD-1", amount=250000,
                               return_url="https://shop.uz/success",
                               account_field_name="order_id")

The part that actually saved me the most time is the webhook side: Django views
you subclass and just implement `successfully_payment` / `cancelled_payment`,
with the signature verification and transaction state-machine handled for you.
There are install extras for Django, FastAPI and Flask.

It's MIT, on PyPI (`pip install unipay-uz`), and has a Russian README since
that's the regional lingua franca.

I'd love feedback on the API shape — especially the gateway factory and the
webhook base classes — and on what a clean test harness for these providers
should look like (sandbox creds are the hard part). Happy to answer anything
about how each gateway's protocol differs.
```

### Tips
- Be in the thread for the first few hours; reply to everything.
- If someone asks "why not just use Stripe?" — the honest answer is *these are
  the rails that actually work in Uzbekistan; Stripe isn't available here.* Say that.
- Don't editorialize the title ("amazing", "the best") — HN hates it.
