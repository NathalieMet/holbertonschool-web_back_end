export default function createInt8TypedArray(length, position, value) {
  if (position < 0 || position >= length) {
    throw new Error('Position outside range');
  }
  const buffer = new ArrayBuffer(length);
  const view = new Int8Array(buffer);
  const dataView = new DataView(buffer);

  view[position] = value;

  return dataView;
}
