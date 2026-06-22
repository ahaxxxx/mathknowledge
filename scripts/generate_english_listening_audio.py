from __future__ import annotations

import argparse
import json
import os
import re
import time
import urllib.error
import urllib.request
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "docs" / "assets" / "audio" / "english-listening"

DEFAULT_MODEL = "gpt-4o-mini-tts"
VOICE = "alloy"

ITEMS = [
    {
        "id": "b2-01-evidence-and-opinion",
        "level": "B2",
        "speed": 0.92,
        "title": "Evidence and Opinion",
        "instructions": (
            "Speak in clear American English at a calm university tutoring pace. "
            "Use careful pauses after contrast words such as however and therefore."
        ),
        "text": """In academic work, an opinion is not rejected simply because it is personal. The problem is that an opinion, by itself, does not give other people a way to check whether it is reliable. Evidence changes the situation. When a writer gives evidence, the reader can ask where the information came from, how it was collected, and whether another explanation is possible. This is why university teachers often ask students to support a claim. They are not asking for more words. They are asking for a visible connection between what you believe and what can be examined. A good reader should therefore listen for three things: the claim, the evidence, and the relationship between them.""",
    },
    {
        "id": "b2-02-defining-a-concept",
        "level": "B2",
        "speed": 0.94,
        "title": "Defining a Concept in a Lecture",
        "instructions": (
            "Speak in clear American English, like a professor introducing a simple concept. "
            "Keep the rhythm steady and make definitions easy to hear."
        ),
        "text": """When a lecturer defines a concept, the definition is usually not the whole explanation. It is the starting point. For example, if a teacher says that a model is a simplified representation of reality, the important question is not only what a model is. The next question is what has been simplified, and why. A map is useful because it leaves out many details. It does not show every tree, every stone, or every person walking on the street. In the same way, an academic model leaves out some features of the world so that one relationship can be studied more clearly. When you listen to a definition, try to hear both parts: the short definition and the reason the definition matters.""",
    },
    {
        "id": "c1-01-correlation-and-causation",
        "level": "C1",
        "speed": 1.0,
        "title": "Correlation and Causation",
        "instructions": (
            "Speak in natural American academic English, a little faster than B2. "
            "Emphasize logical markers such as because, however, and as a result."
        ),
        "text": """One of the most common mistakes in reading empirical research is to treat correlation as causation. If two variables move together, it may be tempting to say that one causes the other. However, the relationship could be produced by a third variable, by the way the data were collected, or by a coincidence within a limited sample. For instance, students who spend more time in the library may also receive higher grades. That observation does not prove that the library itself causes the grades to improve. It may be that more motivated students both study longer and visit the library more often. A careful listener should therefore notice when a speaker moves from describing an association to making a causal claim. That movement requires additional evidence.""",
    },
    {
        "id": "c1-02-assumptions-in-models",
        "level": "C1",
        "speed": 1.0,
        "title": "Assumptions in Mathematical Models",
        "instructions": (
            "Speak in a thoughtful American lecture style. "
            "Use clear pauses around examples and around the final conclusion."
        ),
        "text": """Assumptions in a mathematical model are not decorations. They are the conditions under which the model is allowed to speak. Suppose a model assumes that a population grows at a constant proportional rate. This assumption makes the mathematics cleaner, but it also restricts the situation being described. Real populations may face limited resources, environmental changes, or sudden policy interventions. If those factors are central to the question, the model may still be elegant, but it will no longer be adequate. The point is not that assumptions are bad. Without assumptions, no model can be built. The point is that every conclusion inherits the limits of the assumptions that produced it. In academic listening, phrases such as under the assumption that or provided that are therefore extremely important.""",
    },
    {
        "id": "c2-01-paper-introduction",
        "level": "C2",
        "speed": 1.05,
        "title": "How a Paper Introduction Works",
        "instructions": (
            "Speak in fluent American academic English, like a graduate seminar overview. "
            "Maintain natural speed but keep the argument legible."
        ),
        "text": """A paper introduction rarely begins by telling the reader everything the authors know. Instead, it usually performs a sequence of intellectual moves. First, it identifies a broad area that other researchers already consider important. Then it narrows that area by pointing to a tension, a missing explanation, or a limitation in the existing literature. After that, it states what the present study will contribute. This structure matters because the contribution of a paper is not simply the topic it discusses. The contribution is the difference between what was previously understood and what the paper makes newly visible. When listening to someone summarize an introduction, pay attention to phrases like despite this progress, less is known about, or this paper addresses. These phrases often mark the transition from background knowledge to the research gap.""",
    },
    {
        "id": "c2-02-limitations-and-generalization",
        "level": "C2",
        "speed": 1.06,
        "title": "Limitations and Generalization",
        "instructions": (
            "Speak in natural American English with a polished conference-talk tone. "
            "Use a moderate pace and mark hedging expressions clearly."
        ),
        "text": """In advanced academic writing, limitations are not necessarily weaknesses. A limitation tells the reader how far a conclusion can travel. For example, a study conducted in one city may reveal a mechanism that is relevant elsewhere, but it cannot automatically prove that the same mechanism operates in every cultural or institutional context. This is why researchers often distinguish between internal validity and external validity. Internal validity concerns whether the study supports the conclusion within the case being examined. External validity concerns whether the conclusion can be generalized beyond that case. When a speaker says the results should be interpreted with caution, the point is not to dismiss the study. The point is to locate the boundary of the claim. Strong academic listeners learn to hear those boundaries as part of the argument itself.""",
    },
    {
        "id": "phd-01-ambiguous-findings",
        "level": "PhD",
        "speed": 1.1,
        "title": "Responding to Ambiguous Findings",
        "instructions": (
            "Speak in a realistic American graduate seminar style. "
            "Allow a few hesitations and natural transitions, but keep the recording clean."
        ),
        "text": """I would be a little careful about treating these findings as straightforward evidence for the stronger version of the hypothesis. One interpretation is that the intervention changed the underlying behavior. But another possibility is that it changed what participants thought the researchers expected from them. That distinction matters, because the first interpretation would suggest a real behavioral mechanism, while the second would point to a measurement problem. I am not saying the result is uninteresting. In fact, the ambiguity is partly what makes it useful. It tells us where the next study has to be more precise. For example, we might need a design in which the behavioral outcome is observed indirectly, so that participants have less opportunity to adjust their responses. In that sense, the current result is probably best read as suggestive rather than decisive.""",
    },
    {
        "id": "phd-02-methodological-choice",
        "level": "PhD",
        "speed": 1.1,
        "title": "Defending a Methodological Choice",
        "instructions": (
            "Speak in fluent American academic English, like answering a serious seminar question. "
            "Use natural rhythm, subtle emphasis, and clear stance markers."
        ),
        "text": """That is a fair concern, and I do not think the method solves every problem. The reason we used this design is more limited. We wanted to separate short-term adjustment from longer-term selection effects. A purely cross-sectional comparison would make that distinction almost impossible, because we would not know whether the observed difference existed before the treatment. The panel structure does not eliminate all sources of bias, but it does allow us to ask whether changes within the same unit are consistent with the theoretical mechanism. I would therefore describe the method as a way of reducing one particular ambiguity, not as a guarantee of causal identification. If the question is whether the estimates should be interpreted cautiously, the answer is yes. But if the question is whether the design gives us more information than a static comparison, I think the answer is also yes.""",
    },
]


def load_env(path: Path) -> dict[str, str]:
    values: dict[str, str] = {}
    for raw_line in path.read_text(encoding="utf-8").splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        values[key.strip()] = value.strip().strip('"').strip("'")
    return values


def speech_endpoint(base_url: str) -> str:
    return f"{base_url.rstrip('/')}/audio/speech"


def request_speech(api_key: str, base_url: str, model: str, item: dict[str, object]) -> bytes:
    payload = {
        "model": model,
        "voice": VOICE,
        "input": item["text"],
        "instructions": item["instructions"],
        "response_format": "mp3",
        "speed": item["speed"],
    }
    request = urllib.request.Request(
        speech_endpoint(base_url),
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "audio/mpeg,application/json",
            "User-Agent": "OpenAI-Python/1.0 compatible academic-listening-generator",
        },
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def sanitize_api_error(text: str) -> str:
    text = re.sub(r"sk-[A-Za-z0-9_*.-]+", "[REDACTED_OPENAI_KEY]", text)
    return text[:500]


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--env-file", type=Path)
    parser.add_argument("--output-dir", type=Path, default=OUTPUT_DIR)
    parser.add_argument("--base-url")
    parser.add_argument("--model")
    parser.add_argument("--limit", type=int)
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    env_values = dict(os.environ)
    if args.env_file:
        env_values.update(load_env(args.env_file))
    api_key = env_values.get("OPENAI_API_KEY") or env_values.get("API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY or API_KEY is missing from the env file.")
    base_url = args.base_url or env_values.get("OPENAI_BASE_URL", "https://api.openai.com/v1")
    model = args.model or env_values.get("TTS_MODEL", DEFAULT_MODEL)

    args.output_dir.mkdir(parents=True, exist_ok=True)
    items = ITEMS[: args.limit] if args.limit else ITEMS
    for item in items:
        output_path = args.output_dir / f"{item['id']}.mp3"
        if output_path.exists() and not args.force:
            print(f"skip {output_path.name} already exists")
            continue

        last_error: Exception | None = None
        for attempt in range(3):
            try:
                audio_bytes = request_speech(api_key, base_url, model, item)
                output_path.write_bytes(audio_bytes)
                print(f"wrote {output_path.name} {len(audio_bytes)} bytes")
                break
            except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError) as exc:
                last_error = exc
                if isinstance(exc, urllib.error.HTTPError):
                    details = exc.read().decode("utf-8", errors="replace")
                    print(f"api error for {item['id']}: HTTP {exc.code} {sanitize_api_error(details)}")
                time.sleep(2 + attempt * 3)
        else:
            raise RuntimeError(f"Failed to generate {item['id']}") from last_error


if __name__ == "__main__":
    main()
