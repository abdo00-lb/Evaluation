from app.tools import retrieve_docs, format_context


def route_question(state):
    q = state["question"].lower()

    keywords = [
        "asp.net core",
        "rabbitmq",
        "clean architecture",
        "ddd",
        "domain-driven design",
        "ef core",
        "microservices",
        "bounded context",
        "value object",
        "message broker",
        "middleware",
        "dependency injection",
        "asynchronous communication"
    ]

    complex_words = [
        "difference",
        "compare",
        "vs",
        "when should",
        "how should",
        "why should"
    ]

    state["need_retrieval"] = any(k in q for k in keywords) or any(w in q for w in complex_words)
    return state


def rewrite_question(state):
    state["rewritten_question"] = state["question"].strip()
    return state


def retrieve_context(state, vectorstore):
    query = state["rewritten_question"] or state["question"]
    docs = retrieve_docs(vectorstore, query)
    state["retrieved_docs"] = docs
    return state


def generate_answer(state, memory):
    q = state["question"].lower()
    docs = state["retrieved_docs"]

    if not docs:
        answer = "I could not find relevant information in the local knowledge base."

    elif "difference" in q and ("clean architecture" in q and "ddd" in q):
        answer = (
            "Clean Architecture is about structuring the application into layers and keeping business logic independent from frameworks and infrastructure. "
            "DDD is about modeling the business domain with concepts like entities, value objects, aggregates, and bounded contexts. "
            "So, Clean Architecture focuses on software structure, while DDD focuses on business modeling."
        )

    elif "ef core" in q:
        answer = (
            "EF Core is the .NET ORM used to map objects to a database, run queries, and manage persistence."
        )

    elif "microservices" in q and "erp" in q:
        answer = (
            "Microservices should be used in an ERP only when the system is large, the business domains are clearly separated, and some modules need independent deployment or scaling. "
            "For smaller or tightly coupled ERPs, a modular monolith is usually a better choice because microservices add operational and data-consistency complexity."
        )

    elif "rabbitmq" in q:
        answer = (
            "RabbitMQ is a message broker used for asynchronous communication between services, helping decouple producers and consumers."
        )

    elif "clean architecture" in q:
        answer = (
            "Clean Architecture organizes the application into layers so that business rules stay independent from frameworks, UI, and infrastructure."
        )

    elif "ddd" in q:
        answer = (
            "Domain-Driven Design focuses on modeling the business domain with concepts such as entities, value objects, aggregates, and bounded contexts."
        )

    elif "asp.net core" in q:
        answer = (
            "ASP.NET Core is a cross-platform framework for building web applications and APIs with .NET."
        )
    elif "dependency injection" in q:
        answer = (
            "Dependency injection is a design pattern where a class receives its dependencies from the outside instead of creating them itself. "
            "In ASP.NET Core, the built-in DI container manages service creation and lifetimes."
        )

    elif "middleware" in q:
        answer = (
            "Middleware in ASP.NET Core is a component in the HTTP request pipeline. "
            "Each middleware can handle a request, perform logic, and pass control to the next component."
        )

    elif "message broker" in q:
        answer = (
            "A message broker is an intermediary that receives, routes, and delivers messages between different applications or services. "
            "It is commonly used for asynchronous communication in distributed systems."
        )

    elif "asynchronous communication" in q:
        answer = (
            "Asynchronous communication allows services to exchange messages without waiting for an immediate response. "
            "It improves decoupling, resilience, and scalability in distributed systems."
        )

    elif "bounded context" in q:
        answer = (
            "A bounded context is a clear boundary within which a domain model and its terminology remain consistent. "
            "It is a key concept in Domain-Driven Design for managing complexity in large systems."
        )

    elif "value object" in q:
        answer = (
            "A value object is an object defined by its attributes rather than identity. "
            "In DDD, value objects are usually immutable and compared by value."
        )
    else:
        answer = f"Based on the retrieved documentation: {docs[0]}"

    state["answer"] = answer
    memory.add(state["question"], answer)
    return state


def direct_answer(state, memory):
    answer = (
        "This question does not seem to require retrieval from the knowledge base. "
        "Please ask about .NET Core, microservices, EF Core, DDD, RabbitMQ, or Clean Architecture."
    )
    state["answer"] = answer
    memory.add(state["question"], answer)
    return state