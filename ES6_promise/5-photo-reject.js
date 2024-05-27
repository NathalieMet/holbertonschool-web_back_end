export default function uploadPhoto(filename) {
  const error = new Error(`${filename} cannot be processed`);
  return Promise.reject(error);
}
