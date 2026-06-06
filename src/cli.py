import typer
import json
from src.bot import Bot

app = typer.Typer()


@app.command()
def run(
    url: str = typer.Argument(..., help="URL to fetch and process"),
    max_chunks: int = typer.Option(5, help="Number of chunks to process"),
    output_file: str = typer.Option(None, help="Save results to a JSON file")
):
    """Run the AI pipeline on a given URL."""

    bot = Bot()
    result = bot.run(url, max_chunks=max_chunks)

    print("\n=== Q&A PAIRS ===")
    for i, qa in enumerate(result.qa_pairs):
        print(f"\nQ{i+1}: {qa.question}")
        print(f"A{i+1}: {qa.answer}")

    if output_file:
        data = {
            "source": result.source,
            "status": result.status,
            "total_qa_pairs": len(result.qa_pairs),
            "qa_pairs": [
                {"question": qa.question, "answer": qa.answer}
                for qa in result.qa_pairs
            ]
        }
        with open(output_file, "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n💾 Results saved to {output_file}")


if __name__ == "__main__":
    app()
