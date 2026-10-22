import { randomBytes } from "node:crypto";
import { existsSync, readFileSync, writeFileSync } from "node:fs";

if (!existsSync(".env")) {
  const example = readFileSync(".env.example", "utf8");
  const secret = randomBytes(48).toString("hex");
  const content = example.replace("replace-with-a-random-secret-at-least-32-characters", secret);
  writeFileSync(".env", content, { mode: 0o600 });
  console.log("Created a private .env with a random AUTH_SECRET. Review the developer password before production.");
} else {
  console.log("Using the existing private .env file.");
}
