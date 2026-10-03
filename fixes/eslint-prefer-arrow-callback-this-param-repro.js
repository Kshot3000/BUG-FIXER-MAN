// Repro for eslint/eslint#21155 — prefer-arrow-callback reports a function
// expression that declares a TypeScript `this` parameter. Arrow functions
// cannot declare a `this` parameter, so the report is invalid (and any fix
// would produce syntactically invalid TS).
const { Linter } = require("./lib/linter/linter.js");

const code = `
function acceptsCb(cb) {}
class Foo {}
acceptsCb(function (this: Foo) {})
acceptsCb(function (this: Foo, x) { return x; })
acceptsCb(function (x) { return x; })
`;

const linter = new Linter();
const messages = linter.verify(
	code,
	[
		{
			files: ["**/*.ts"],
			languageOptions: {
				parser: require("@typescript-eslint/parser"),
				parserOptions: { ecmaFeatures: { jsx: true } },
			},
			rules: { "prefer-arrow-callback": "error" },
		},
	],
	{ filename: "repro.ts" },
);

console.log(JSON.stringify(messages, null, 2));
const bad = messages.filter(m => m.line <= 4);
if (bad.length) {
	console.log("BUG REPRODUCED: `this`-param callbacks were reported:", bad.map(m => `line ${m.line}`).join(", "));
	process.exit(1);
}
console.log("OK: no report for `this`-param callbacks (plain-param callback on line 5 should still be reported).");
