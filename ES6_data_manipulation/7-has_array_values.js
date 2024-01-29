export default function hasValuesFromArray(set, array) {
  return Array.from(array).every((value) => set.has(value));
}
