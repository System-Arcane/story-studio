import type { Metadata } from 'next';
import './globals.css';
export const metadata: Metadata = { title: 'STory — 당신의 상품에, 이야기를.', description: '사진 한 장에서 시작되는 30초의 이야기. STory 광고 제작 스튜디오.' };
export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) { return <html lang="ko"><body>{children}</body></html>; }
